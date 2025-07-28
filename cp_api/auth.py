import jwt
import requests
from functools import wraps
from flask import request, jsonify, g


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"message": "Missing or invalid Authorization header"}), 401

        token = auth.split(" ", 1)[1]
        # Fetch Keycloak JWKS
        jwks_url = "http://localhost:8081/realms/chronos-realm/protocol/openid-connect/certs"
        jwks = requests.get(jwks_url).json()
        untrusted_header = jwt.get_unverified_header(token)
        key = next(
            (k for k in jwks["keys"] if k["kid"] == untrusted_header["kid"]),
            None
        )
        if key is None:
            return jsonify({"message": "Public key not found"}), 401

        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
        try:
            # verify signature, expiration, and audience
            payload = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                audience="chronos-swagger-client"
            )
            # store client_id (authorized party) in g
            g.client_id = payload.get("azp") or payload.get("client_id")
        except Exception as e:
            return jsonify({"message": f"Token error: {str(e)}"}), 403

        return f(*args, **kwargs)
    return decorated

from fastapi import FastAPI, Header, Request
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from starlette.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
#async def read_root(x_ssl_cert: str = Header(None)):
async def read_root(request: Request):
    #return {"message": "Hello World"}
    x_ssl_cert = request.headers.get("X-SSL-Cert")
    cert_fields = {}
    fields = x_ssl_cert.split(",")

    for field in fields:
        key, value = field.split("=")
        cert_fields[key.strip()] = value.strip()

    return cert_fields
    #return x_ssl_cert
    if x_ssl_cert is None:
        return JSONResponse(content={"error": "Client certificate header not found"}, status_code=400)
    
    try:
        cert_bytes = bytes.fromhex(x_ssl_cert)
        cert = x509.load_der_x509_certificate(cert_bytes, default_backend())
        cert_subject = cert.subject.rfc4514_string()
        cert_issuer = cert.issuer.rfc4514_string()
        
        return {
            "message": "Client certificate successfully parsed",
            "subject": cert_subject,
            "issuer": cert_issuer
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

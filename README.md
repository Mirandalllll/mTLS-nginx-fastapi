# mTLS-nginx-fastapi
This project is a Docker environment used for experimenting with mTLS in nginx. Nginx serves as a reverse proxy for FastAPI in this implementation. This project was created when researching the user experience with TLS Client Authentication and mTLS. It was later applied to an actual server accessed by students in the course COSC483/583 Applied Cryptography at the Univeristy of Tennessee, Knoxville for data collection.

## How to Setup
1. Clone this repository
2. Docker is required, the entire project runs inside of Docker.
3. Create certificates using OpenSSL or any certificate creation tool of your choice. You will need the following:
   ```
    ca.pem
    ca-key.pem
    server.pem
    server-key.pem
    client.pem
    client-key.pem
   ```
   Place these files in the nginx/certs/ folder.
4. Inspect the nginx configuration file found in the nginx folder. If you would like to use an existing domain that you own. You will need to edit this file and replace localhost with the correct domain and/or IP address.
5. Run the Docker container by navigating to the base directory and running `$docker-compose up --build`. This will build and run the container.
6. In order to pass the client certificate verification when navigating to the server you must first upload your client certificate chain to your browser choice in .p12 format. Once this is completed, you may also want to upload your CA certificate chain in .p12 format to your browser of choice. Consult your browser for instructions on how to upload these certificate chains.
7. Navigate to `https://localhost` (or the domain you choose), supply the client certificate chain when prompted. The fastapi application will parse the certificate supplied and output in the browser. 

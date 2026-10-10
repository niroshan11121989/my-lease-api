from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

# 1. This is your login system
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    # CHANGE THESE TO YOUR DESIRED USERNAME AND PASSWORD
    correct_username = "admin"
    correct_password = "password123"
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# 2. This is your public "Hello World" to test if it works
@app.get("/")
def read_root():
    return {"message": "Lease API is running!"}

# 3. This is a protected route. Only users with username/password can see this.
@app.get("/leases")
def get_leases(user: str = Depends(authenticate)):
    return {
        "message": "Welcome to your Lease Data Entry System!",
        "logged_in_as": user,
        "data": [
            {"s_no": "KL/2026/0001", "applicant": "S.E.Jeyarajah", "status": "Active"}
        ]
    }
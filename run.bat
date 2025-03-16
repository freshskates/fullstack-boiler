@echo off
echo "Copying env sample files..."

copy frontend\.env.sample frontend\.env
copy backend\.env.sample backend\.env

cd backend 

@REM echo "Creating Python venv"
@REM python -m venv .venv

echo "Installing uv..."
pip install uv

echo "Creating virtual environment..."
uv venv 

echo "Activating virtual environment..."
call .venv\Scripts\activate

echo "Installing requirements with uv venv..."
uv sync

echo "Generating DB schema..."
prisma generate

echo "You can now run the backend server with:"
echo "uv run task dev"

cd .. 

echo "Installing frontend dependencies..."
cd frontend

echo "Installing node modules..."
npm install

echo "You can now run the frontend server with:"
echo "npm run dev"

cd ..

echo "Done"
pause

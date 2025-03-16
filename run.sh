#!/bin/bash

echo "Copying env sample files..."

cp ./frontend/.env.sample ./frontend/.env
cp ./backend/.env.sample ./backend/.env

cd backend || exit

# echo "Creating Python venv"
# python -m venv venv

echo "Installing uv..."
pip install uv

echo "Creating virtual environment..."
uv venv 

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing requirements with uv venv..."
uv sync

echo "Generating db schema..."
prisma generate

echo "You can now run the backend server with:"
echo "uv run task dev"

cd .. || exit

echo "Installing frontend dependencies...."
cd frontend || exit

echo "Installing node modules...."
npm install

echo "You can now run the frontend server with:"
echo "npm run dev"

cd .. || exit

echo "Done"

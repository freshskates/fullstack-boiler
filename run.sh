#!/bin/bash

echo "copying env sample files.."

cp ./frontend/.env.sample ./frontend/.env
cp ./backend/.env.sample ./backend/.env

cd backend || exit

echo "installing uv.."
pip install uv

echo "creating virtual environment.."
uv venv 

echo "activating virtual environment.."
source .venv/bin/activate

echo "installing requirements with uv venv.."
uv sync

echo "generating db schema.."
prisma generate

echo "you can now run the backend server with"
echo "uv run task dev"

cd .. || exit

echo "installing frontend dependencies..."
cd frontend || exit

echo "installing node modules..."
npm install

echo "you can now run the frontend server with"
echo "npm run dev"

cd .. || exit

echo "done"

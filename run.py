import platform
import queue
import subprocess
from typing import List, Tuple, Union
from pathlib import Path

COMMAND_LOGICAL_AND_OPERATOR = "&&"
CURRENT_WORKING_DIRECTORY = Path.cwd()

class CommandHandler:
    """
    Works 
        Windows
            CMD
        Unix Like and Unix
            Bash

    """

    _counter = int
    pq_arguments: queue.PriorityQueue[Tuple[int, str]]
    pq_arguments_cmd: queue.PriorityQueue[Tuple[int, str]]
    pq_arguments_bash: queue.PriorityQueue[Tuple[int, str]]

    def __init__(self):

        self._counter = 0
        self.pq_arguments = queue.PriorityQueue(maxsize=0)
        self.pq_arguments_cmd = queue.PriorityQueue(maxsize=0)
        self.pq_arguments_bash = queue.PriorityQueue(maxsize=0)

    def add_argumenet(self, argument: str):
        self.pq_arguments.put((self._counter, argument))
        self._counter += 1

    def add_argumenet_cmd(self, argument: str):
        self.pq_arguments_cmd.put((self._counter, argument))
        self._counter += 1

    def add_argumenet_bash(self, argument: str):
        self.pq_arguments_bash.put((self._counter, argument))
        self._counter += 1

    def run(self):

        arguments = []
        if platform.system() == "Windows":
            while not self.pq_arguments_cmd.empty():
                self.pq_arguments.put(self.pq_arguments_cmd.get())

        else:  # Not Windows
            while not self.pq_arguments_bash.empty():
                self.pq_arguments.put(self.pq_arguments_bash.get())

        while not self.pq_arguments.empty():
            arguments.append(self.pq_arguments.get()[1])

        execution_string: str = f" {COMMAND_LOGICAL_AND_OPERATOR} ".join(
            arguments
        )

        for i in arguments:
            print(i)

        # subprocess.run(execution_string, shell=True)

# ------------ Sequence of Commands Start ------------


command_handler = CommandHandler()

command_handler.add_argumenet(fr'cd "{CURRENT_WORKING_DIRECTORY}"')
command_handler.add_argumenet(r'echo "Copying env sample files..."')

command_handler.add_argumenet_cmd(r'copy frontend\.env.sample frontend\.env')
command_handler.add_argumenet_cmd(r'copy backend\.env.sample backend\.env')
command_handler.add_argumenet_bash(r'cp ./frontend/.env.sample ./frontend/.env')
command_handler.add_argumenet_bash(r'cp ./backend/.env.sample ./backend/.env')

command_handler.add_argumenet(r'cd backend')

# command_handler.add_argumenet(r'echo "Creating Python venv"')
# command_handler.add_argumenet(r'python -m venv venv')

command_handler.add_argumenet(r'echo "Installing uv..."')
command_handler.add_argumenet(r'pip install uv')

command_handler.add_argumenet(r'echo "Creating virtual environment..."')
command_handler.add_argumenet(r'uv venv')

command_handler.add_argumenet(r'echo "Activating virtual environment..."')
command_handler.add_argumenet_cmd(r'call .venv\Scripts\activate')
command_handler.add_argumenet_bash(r'source .venv/bin/activate')

command_handler.add_argumenet(r'echo "Installing requirements with uv venv..."')
command_handler.add_argumenet(r'uv sync')

command_handler.add_argumenet(r'echo "Generating DB schema..."')
command_handler.add_argumenet(r'prisma generate')

command_handler.add_argumenet(r'echo "You can now run the backend server with:"')
command_handler.add_argumenet(r'echo "uv run task dev"')

command_handler.add_argumenet(r'cd .. ')

command_handler.add_argumenet(r'echo "Installing frontend dependencies..."')
command_handler.add_argumenet(r'cd frontend')

command_handler.add_argumenet(r'echo "Installing node modules..."')
command_handler.add_argumenet(r'npm install')

command_handler.add_argumenet(r'echo "You can now run the frontend server with:"')
command_handler.add_argumenet(r'echo "npm run dev"')

command_handler.add_argumenet(r'cd ..')

command_handler.add_argumenet(r'echo "Done"')
# command_handler.add_argumenet_cmd(r'pause')

# ------------ Sequence of Commands End ------------


command_handler.run()

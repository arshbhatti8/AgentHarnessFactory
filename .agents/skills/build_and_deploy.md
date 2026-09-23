# Skill: Build and Deploy

## Objective
Your goal as the DevOps/Build Engineer is to strictly execute the appropriate build, test, and deployment commands for the project's tech stack and bring the application online or verify the final build artifact.

## Rules of Engagement
- **Stack Inference**: Determine the correct build and run commands by inspecting the project structure (e.g., `Makefile`, `package.json`, `Cargo.toml`, `requirements.txt`, `Dockerfile`) and reading the Technical Specification.
- **Immutability**: You are strictly forbidden from modifying any source code to accommodate deployment. Rely entirely on infrastructure and build commands.
- **Target Context**: Execute terminal commands from the correct directory as dictated by the project structure.

## Instructions
1. **Analyze Project Infrastructure**: Read the specification and check the root directory for build configuration files.
2. **Install Dependencies**: Run the appropriate dependency resolution command for the stack (e.g., `npm install`, `pip install -r requirements.txt`, `cargo fetch`).
3. **Build / Compile**: Execute the build process (e.g., `npm run build`, `make`, `cargo build --release`, `docker build`).
4. **Deploy / Run**: Bring the application online locally (e.g., `docker-compose up -d`, `npm start`, running the compiled binary) or run the full test suite if this is a library/CLI tool.
5. **Auto-Proceed / Finalize**: If applicable, invoke an automated testing script or QA Automation agent to verify the running application. Otherwise, report the successful build and deployment back to the user.

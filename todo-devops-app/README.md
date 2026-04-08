# To-Do DevOps App (SEA Lab)

A simple Flask-based To-Do app with automated CI using GitHub Actions.

## Project Structure

```
todo-devops-app/
|-- app.py
|-- requirements.txt
|-- test_app.py
|-- templates/
|   `-- index.html
`-- .github/
    `-- workflows/
        `-- ci.yml
```

## Run Locally

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open:

`http://127.0.0.1:5000/`

## Run Tests

```bash
pytest -q
```

## CI/CD

The GitHub Actions workflow in `.github/workflows/ci.yml` automatically:

- Installs dependencies
- Runs tests on push and pull requests to `main`

The same workflow also includes an optional deploy stage for pushes to `main`.
If you add a repository secret named `RENDER_DEPLOY_HOOK_URL`, it will trigger deployment using that hook URL.

## Push To GitHub

Run these commands from the `todo-devops-app` folder:

```bash
git init
git add .
git commit -m "Initial Flask app with CI/CD"
git branch -M main
git remote add origin https://github.com/<your-username>/todo-devops-app.git
git push -u origin main
```

# Docker environments 

## CodeBook 

### Docker Build and Run

Change to the `docker` directory so that the docker build context is the current working directory. Create a `.env` file and the change any variables as necessary, then source those variables for later use.

```bash
cd docker
cat <<-EOF > .env
COMPOSE_PROJECT_NAME=datajoint-workflow-neuro
JHUB_VER=1.4.2
PY_VER=3.9
DIST=debian
DEPLOY_KEY=o-science-institute_w-neuro-lab-deploy.pem
REPO_OWNER=dj-sciops
REPO_NAME=o-science-institute_w-neuro-lab
WORKFLOW_VERSION=v0.0.1
HOST_UID=1000
EOF
set +a 
source .env
set -a
```

```bash
docker build \
  $(cat .env | while read li; do echo --build-arg ${li}; done | xargs) \
  --file codebook.Dockerfile \
  --tag registry.vathes.com/${REPO_OWNER}/codebook-${REPO_NAME}:jhub${JHUB_VER}-py${PY_VER}-${DIST}-${WORKFLOW_VERSION} \
  .
```

```bash
docker run -it \
  --platform linux/amd64 \
  --name datajoint-workflow-neuro \
  --user root \
  registry.vathes.com/${REPO_OWNER}/codebook-${REPO_NAME}:jhub${JHUB_VER}-py${PY_VER}-${DIST}-${WORKFLOW_VERSION} \
  bash
```

### Docker Compose 

Will automatically load environment variables from `.env` file. 

```bash 
cd docker
export COMPOSE_PROJECT_NAME=datajoint-workflow-neuro
docker-compose -f docker-compose-codebook_env.yaml up --build -d
```

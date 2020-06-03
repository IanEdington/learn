# Local dev environment

Goals:

1. declutter local workspaces
1. practice infrastructure as code
1. working environment similar to Sagemaker (used by Faire)
1. 


## Run notebook locally and kernels in docker container
I really didn't want to install conda on my machine since the last time I did that it was difficult to switch back and forth between it and venv ect.

This is an attempt to run the Jupyter notebook in the mac environment and the kernels in a docker contains.
Hopefully this will be cleaner than installing conda locally and easier to spin up than sagemaker.

The above didn't work because kernels need more context than can be given over a network connection.

## Use docker environment and attach a local folder
Next I'm trying to use docker as a stand alone environment mounting the whole machine learning repo

Run from folder to be mounted
```bash
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/tensorflow-notebook
```

This seems to be working a lot better but requires a manual process to reproduce

## Terraform the environment

Going through the tutorial and documentation seems to be straight forward.

Terraform is up and running.

running `terraform apply` will install the docker container

running `terraform destroy` will tear it down

## Future improvements
A possible improvement would be to use a Sagemaker env locally as described here:
- https://booklet.ai/blog/aws-sagemaker-pytorch-local-dev-flow/
- https://sagemaker.readthedocs.io/en/stable/overview.html

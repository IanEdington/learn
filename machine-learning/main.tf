terraform {
  required_providers {
    docker = "~> 2.7"
  }
}

resource "docker_image" "jupyter-tensorflow-notebook" {
  name         = "jupyter/tensorflow-notebook:latest"
  keep_locally = true
}

resource "docker_container" "data-science" {
  name    = "data-science"
  image   = docker_image.jupyter-tensorflow-notebook.latest
  env     = ["JUPYTER_ENABLE_LAB=yes"]
  command = ["start.sh", "jupyter", "lab", "--LabApp.token=''"]

  mounts {
    type   = "bind"
    target = "/home/jovyan/work"
    source = abspath(".")
  }
  ports {
    internal = 8888
    external = 8888
  }
}

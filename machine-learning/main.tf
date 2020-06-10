terraform {
  required_providers {
    docker = "~> 2.7"
  }
}

resource "docker_image" "jupyter-lab-kitted-out" {
  name         = "jupyter-lab-kitted-out:latest"
  keep_locally = true
}

resource "docker_container" "data-science" {
  name    = "data-science"
  image   = docker_image.jupyter-lab-kitted-out.latest
  env     = ["JUPYTER_ENABLE_LAB=yes"]
  command = ["start.sh", "jupyter", "lab", "--LabApp.token=''"]

  mounts {
    type   = "bind"
    source = abspath(path.root)
    target = "/home/jovyan/work"
  }
  volumes {
    host_path      = "/Users/ian/.jupyter/lab/user-settings"
    container_path = "/home/jovyan/.jupyter/lab/user-settings"
  }
  ports {
    internal = 8888
    external = 8888
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
resource "google_compute_instance" "example" {
  name         = "example-instance"
  machine_type = var.machine_type
  zone         = var.zone
  boot_disk {
    initialize_params {
      image = var.image
    }
  }
}

# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-docker-compose")
  raise "Docker-compose can not be run! Install plugin using 'vagrant plugin install vagrant-docker-compose' and rerun!"
end


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8888

  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.dev.yml", rebuild: true, run: "always"
end

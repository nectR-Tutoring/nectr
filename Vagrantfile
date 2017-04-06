# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-docker-compose")
  raise "Docker-compose can not be run! Install plugin using 'vagrant plugin install vagrant-docker-compose' and rerun!"
end


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  # Forward ports as needed. This should be good for most setups
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8888
  config.vm.network "forwarded_port", guest: 2376 , host: 2376

  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.dev.yml", rebuild: true, run: "always"
  # config.vm.provision "shell", path: "/vagrant/utility/docker_external_setup.sh"
end

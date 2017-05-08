# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
unless Vagrant.has_plugin?("vagrant-docker-compose")
  raise "Docker-compose can not be run! Install plugin using 'vagrant plugin install vagrant-docker-compose' and rerun!"
end


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  # Forward ports as needed. This should be good for most setups
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8888
  config.vm.network "forwarded_port", guest: 8025, host: 8025

  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.vagrant.dev.yml", rebuild: true, run: "always"

end




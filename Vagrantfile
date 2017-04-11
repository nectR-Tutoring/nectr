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
  # config.vm.box = "ubuntu/trusty64"
  # config.vm.network "private_network", ip: "192.168.50.4"
  # Forward ports as needed. This should be good for most setups
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 8000, host: 8888
  # config.vm.network "forwarded_port", guest: 2375 , host: 2376

  # config.vm.provider "hyperv"
  # config.vm.provider "virtualbox"


  #config.vm.provision "shell", path: "utility/docker_external_setup.sh", privileged: true
  #config.vm.provision "shell", inline: <<-SHELL
  #  sudo apt-get update
  #  sudo apt-get install -y software-properties-common curl
  #  sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
  #  sudo echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list
  #  sudo apt-get update
  #  sudo apt-get purge lxc-docker
  #  sudo apt-cache policy docker-engine
  #  sudo apt-get install -y linux-image-extra-$(uname -r)
  #  sudo apt-get install -y docker-engine
  #  sudo echo 'DOCKER_OPTS="-H tcp://127.0.0.1:4243 -H unix:///var/run/docker.sock"' >> /etc/default/docker
  #  sudo service docker restart
  #  sudo usermod -aG docker vagrant
  #  echo 'export DOCKER_HOST=tcp://localhost:4243' >> /home/vagrant/.bashrc
  # curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` -o docker-compose
  #  sudo chmod +x docker-compose
  #  sudo mv docker-compose /usr/local/bin
  #SHELL
  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.dev.yml", rebuild: true, run: "always"
  config.vm.provision "shell", inline: "docker -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock -d &"

end

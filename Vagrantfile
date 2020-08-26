# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.disksize.size = "1GB"
  config.ssh.insert_key = false
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  # for Docker on Vagrant
  config.vm.provision :docker, run: 'always'
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml"
end

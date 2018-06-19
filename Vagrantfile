# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant configuration
Vagrant.configure(2) do |config|
  # CentOS 6.x base box
  config.vm.box = "cedadev/centos6"

  config.vm.network "private_network", ip: "192.168.51.35"

  config.vm.provision :shell, inline: <<SHELL
set -x

mkdir -p /root/.ssh
cp ~vagrant/.ssh/authorized_keys /root/.ssh

cat > /etc/selinux/config <<-SELINUXCONF
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#       enforcing - SELinux security policy is enforced.
#       permissive - SELinux prints warnings instead of enforcing.
#       disabled - SELinux is fully disabled.
SELINUX=disabled
# SELINUXTYPE= type of policy in use. Possible values are:
#       targeted - Only targeted network daemons are protected.
#       strict - Full SELinux protection.
SELINUXTYPE=targeted
SELINUXCONF
SHELL

  # Disabling SELinux requires a reboot
  #   Requires "vagrant plugin install vagrant-reload"
  config.vm.provision :reload

  require "yaml"
  if File.exists?(".superuser-variables")
    superuser = YAML.load_file('.superuser-variables')
  else
    superuser = {}
    print "Username for Django superuser: "
    superuser['username'] = STDIN.gets.chomp
    print "Email address for Django superuser: "
    superuser['email'] = STDIN.gets.chomp
    print "Password for Django superuser: "
    superuser['password'] = STDIN.noecho(&:gets).chomp
    puts ""
    File.open(".superuser-variables", "w") do |file|
      file.write(superuser.to_yaml)
    end
  end

  config.vm.provision :ansible do |ansible|
    ansible.force_remote_user = false
    ansible.playbook = "playbook/playbook.yml"
    ansible.config_file = "playbook/ansible.cfg"
    ansible.galaxy_role_file = "playbook/requirements.yml"
    ansible.galaxy_roles_path = "playbook/.roles"
    ansible.extra_vars = {
      "prompt_superuser_username" => "#{superuser['username']}",
      "prompt_superuser_email"    => "#{superuser['email']}",
      "prompt_superuser_password" => "#{superuser['password']}",
      "private_ip_address" => "#{'192.168.51.35'}",
    }
  end
end

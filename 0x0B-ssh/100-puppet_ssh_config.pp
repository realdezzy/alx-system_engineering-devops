file { '/root/.ssh/config' :
  ensure  => file,
  content => "
      Host realdezzy.tech
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
        PubkeyAuthentication yes
        StrictHostKeyChecking no
        "
}

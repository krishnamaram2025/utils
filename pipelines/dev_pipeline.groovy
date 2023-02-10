

deployrepo = "https://github.com/krishnamaram2025/utils.git"
deployreponame = "utils"
Dir = "${deployreponame}/aws"
pipeline {

agent any
   
environment {
    AWS_ACCESS_KEY_ID = credentials('access_key_id')
    AWS_SECRET_ACCESS_KEY = credentials('secret_key_id')
    }

parameters {
    string(name: "Task", description: "task", defaultValue: "create")
    string(name: "Branch_Name", description: "branch", defaultValue: "master")
}

stages {
stage('Cloning Git') {
steps {
git branch: 'master', url: 'https://github.com/krishnamaram2025/utils.git'
}
}
stage('running script') {
steps{
script {
sh """
 whoami
 export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
 export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
 sudo yum install python3-pip -y
 sudo pip3 install -r requirements.txt
 cd aws && sudo python3 iam.py 
"""
}
}
}
}

}

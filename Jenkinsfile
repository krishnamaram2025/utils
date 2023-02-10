
pipeline {

agent any

parameters {
    string(name: "accesskey", description: "accesskey")
    string(name: "secretkey", description: "secretkey")
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
 echo '${params.accesskey}' 
 echo '${params.secretkey}'
 sudo yum install python3-pip -y
 sudo pip3 install -r requirements.txt
 cd aws && sudo python3 vpc.py '${params.accesskey}' '${params.secretkey}' 
"""
}
}
}
}

}

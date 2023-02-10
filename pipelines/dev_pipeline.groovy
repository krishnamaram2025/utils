

deployRepo = "https://github.com/krishnamaram2025/utils.git"
deployRepoName = "utils"
Dir = "${deployRepoName}/cloud_operations/aws"
pipeline {
agent any
   
environment {
    AWS_ACCESS_KEY_ID = credentials('access_key_id')
    AWS_SECRET_ACCESS_KEY = credentials('secret_key_id')
    }

parameters {
    string(name: "Task", description: "task", defaultValue: "create")
    string(name: "BRANCH_NAME", description: "branch", defaultValue: "master")
}

stages {
   
stage('Cloning Git') {
steps {
   script{
gitClone()
   }
}
}
   
stage('running script') {
steps{
script {
sh """
 whoami
 echo ${AWS_ACCESS_KEY_ID}
 export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
 export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
 sudo yum install python3-pip -y
 sudo pip3 install -r requirements.txt
 cd ${Dir} && sudo python3 iam.py 
"""
}
}
}
} 
}
   
// Clone Utils repo
def gitClone() {
   dir(deployRepoName) {
      git branch: params.BRANCH_NAME, url: deployRepo
}

}

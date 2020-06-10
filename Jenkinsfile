pipeline{
    agent any
    stages{

            stage('Dependencies'){
                steps{
                    sh 'chmod +x ./script/*'
                    sh 'bash ./script/installationbefore.sh'
                    sh './script/ansible.sh'
                }
            }

            stage('Deploying Docker Stack'){
                steps{
                    sh 'chmod +x ./script/*'
                    sh './script/swarmstack.sh'
                }
            }

    }
}
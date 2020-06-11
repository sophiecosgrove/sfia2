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
                environment{
                    DATABASE_URI="${DATABASE_URI}"
                }
                steps{
                    sh 'export DATABASE_URI'
                    sh 'chmod +x ./script/*'
                    sh './script/swarmstack.sh'
                }
            }

    }
}
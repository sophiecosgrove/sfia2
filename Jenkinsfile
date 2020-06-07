pipeline{
    agent any
    stages{
        stage("Make scripts executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Source bash variables"){
            steps{
                sh './script/sourcebash.sh'
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './script/swarmstack.sh'
            }
        }
    }
}
pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw1_rotate.py -i cameraman.jpg -t 0.5'
                sh 'python dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m bilinear'
                sh 'python dip_hw1_rotate.py -i cameraman.jpg -t -0.5'
                sh 'python dip_hw1_rotate.py -i cameraman.jpg -t 2 -m bilinear'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}
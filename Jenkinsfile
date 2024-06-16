pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    stages {
        stage('Run tests') {
            steps {
                sh '''
                    python3 test_calculator.py
                '''
            }
        }
    }
    post {
        success {
            echo 'Testy przebiegły bezproblemowo!'
        }
        failure {
            echo 'Słabo ... coś się zepsuło.'
        }
    }
}

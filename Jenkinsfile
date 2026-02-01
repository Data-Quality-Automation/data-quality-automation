pipeline {
    agent any

    triggers {
        cron('H 1 * * *')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute Data Quality Regression') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
        failure {
            echo 'Data quality validation failed – investigate discrepancies'
        }
    }
}

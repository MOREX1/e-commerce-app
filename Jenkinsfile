pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'  // إنشاء بيئة افتراضية
                sh '. venv/bin/activate && pip install -r requirements.txt'  // تثبيت المتطلبات
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest tests/'  // تشغيل الاختبارات
            }
        }
    }
}


stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            sh '. venv/bin/activate && sonar-scanner -Dsonar.projectKey=e-commerce-app -Dsonar.host.url=http://localhost:9000 -Dsonar.login=<sqa_b49648dacaabe3dd318676eb9b2c92dc57e0bc70>'
        }
    }
}

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

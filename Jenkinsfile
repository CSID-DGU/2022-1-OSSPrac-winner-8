node {
	git poll: true, url:'https://github.com/wlgus5704/2022-1-OSSPrac-winner-8.git'
	withCredentials([[$class: 'UsernamePasswordMultiBinding',
	credentialsId: 'docker-hub',
	usernameVariable: 'DOCKER_USER_ID',
	passwordVariable: 'DOCKER_USER_PASSWORD']]) {
		stage('Pull') {
			git 'https://github.com/wlgus5704/2022-1-OSSPrac-winner-8.git'
		}
		stage('Unit Test') {
		}
		stage('Build') {
			sh(script: 'docker-compose --build')
		}
		stage('Tag') {
			sh(script: '''docker tag ${DOCKER_USER_ID}/ossprac \
			${DOCKER_USER_ID}/ossprac:${BUILD_NUMBER}''')
		}
		stage('Push') {
			sh(script: 'docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}')
			//sh(script: 'docker push ${DOCKER_USER_ID}/ossprac:${BUILD_NUMBER}')
			sh(script: 'docker push ${DOCKER_USER_ID}/ossprac:latest')
		}
		stage('Deploy') {
			sh(script: 'docker-compose up -d production')
		}
		}
	}
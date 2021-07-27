pipeline {

  agent any 

  stages {

    stage ('Molecule test') {
      steps {
        sh '''
          molecule test
        '''
      }
    }

    stage ('Deploy the shit to another machine') {
      steps {
        sh '''
          scp -r /tmp/scptest/ 192.168.0.36:/tmp/
        '''
      }
    }

  }
}

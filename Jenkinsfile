pipeline {

  agent {
    label 'agent'
  }

  stages {
    
    stage ('Setup Python virtual environment') {
      steps {
        sh '''
          pip3.6 install virtualenv
          virtualenv virtenv
          source virtenv/bin/activate
          python3 -m pip install --upgrade ansible molecule
        '''
      }
    }
    
    stage ('Display versions') {
      steps {
        sh '''
          source virtenv/bin/activate
          python -V
          ansible --version
          molecule --version
        '''
      }
    }    

    stage ('Molecule test') {
      steps {
        sh '''
          source virtenv/bin/activate
          molecule test
        '''
      }
    }
  }
}

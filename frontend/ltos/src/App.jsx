import './styles/App.css';
import Header from './components/header.jsx';
import Main from './components/Main.jsx';
import SignupForm from './components/SignupForm.jsx';
import Login from './components/Login.jsx';
import UploadVideo from './components/UploadVideo.jsx';

function App() {
  return (
    <div className='App'>
      <Header></Header>
      <UploadVideo></UploadVideo>
    </div>
  );
}

export default App;

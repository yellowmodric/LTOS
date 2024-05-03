import '../styles/Login.css';
import React, {useState} from 'react';

function Login() {
    const [userId, setUserId] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(userId, password);
    };

    const handleForgotId = () => {
        console.log('아이디 찾기');
    }

    const handleForgotPassword = () => {
        console.log('비밀번호 찾기');
    }

    const handleSignUp = () => {
        console.log('회원가입');
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>로그인</h1>
            <input type='text' placeholder='아이디를 입력해 주세요' id='userId' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='password' placeholder='비밀번호를 입력해 주세요' id='password' value={password} onChange={(e) => setPassword(e.target.value)}/>
            <button className='submit-log' type='submit'>로그인</button>
            <div className='find-container'>
                <button onClick={handleForgotId}>아이디 찾기</button>
                |
                <button onClick={handleForgotPassword}>비밀번호 찾기</button>
            </div>
            <button className='move-sign' onClick={handleSignUp}>회원가입</button>
        </form>

    )
}

export default Login;
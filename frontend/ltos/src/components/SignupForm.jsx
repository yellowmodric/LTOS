import '../styles/sign.css';
import React, {useState} from 'react';

function SignupForm() {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        confirmPassword: '',
        email: '',
        emailDomain: 'naver.com',
    });

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value,
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);
    };

    function checkUserId() {
        console.log('checking');
    }

    return (
        <section className="signature">
            <h1>회원 가입</h1>
            <form className="sign-form" onSubmit={handleSubmit}>
                <div className="input-container">
                    <input type="text" className='input-id' placeholder="아이디 입력" name='username' value={formData.username} onChange={handleChange}/>
                <button className="btn-idCheck" onClick={checkUserId}>중복 확인</button>
                </div>
                <input type="password" placeholder="비밀번호 입력" name='password' value={formData.password} onChange={handleChange}/>
                <input type="password" placeholder="비밀번호 재입력" name='confirmPassword' value={formData.confirmPassword} onChange={handleChange}/>
                <div className="input-container-email">
                    <input type="text" placeholder="이메일 주소" name='email' value={formData.email} onChange={handleChange}/>
                    @
                    <select className="emailDomain" name='emailDomain' value={formData.emailDomain} onChange={handleChange}>
                        <option value="naver.com">naver.com</option>
                        <option value="gmail.com">gmail.com</option>
                        <option value="daum.net">daum.net</option>
                    </select>
                </div>
                <div className="submit-container">
                    <button className='submit' type="submit" value="가입하기">가입하기</button>
                </div>
            </form>
        </section>
    );
}


export default SignupForm;
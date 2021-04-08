var signinBtn, popupForm, closeBtn;

signinBtn = document.querySelector('.Signin-btn');
popupForm = document.querySelector('.popup-container');
closeBtn = popupForm.querySelector('.close-btn');

//event handle to show hidden form
signinBtn.addEventListener('click', () => {
	//remove hide class from popupForm
	popupForm.classList.remove('hide');
});

closeBtn.addEventListener('click', () => {
    popupForm.classList.add('hide');
});

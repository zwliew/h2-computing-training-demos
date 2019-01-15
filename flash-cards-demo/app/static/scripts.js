function handleCardClick(event) {
  const id = event.target.id;
  if (id === 'card-test-input' || id === 'card-test-submit') return;
  const target = event.currentTarget;
  const frontDiv = target.getElementsByClassName('card-front')[0];
  const backDiv = target.getElementsByClassName('card-back')[0];
  frontDiv.toggleAttribute('hidden');
  backDiv.toggleAttribute('hidden');
}

function handleGuessClick(event) {
  const testParent = event.target.closest('.card-test');
  const answer = testParent.dataset.answer;
  const input = testParent.querySelector('#card-test-input');
  if (answer.trim() === input.value.trim()) {
    event.target.classList.add('card-test-submit-success');
    input.value = 'You got it right!';
  } else {
    event.target.classList.add('card-test-submit-hmmmmmmmmmmm🤔');
    const curValue = input.value;
    input.value = '🤔';
    setTimeout(() => {
      input.value = curValue;
      event.target.classList.remove('card-test-submit-hmmmmmmmmmmm🤔');
    }, 300);
  }
  event.stopPropagation();
}
function countUpFromZero(zero){
	if(zero == 10){
		return;
	}
	zero++;
	console.log(zero);
	return countUpFromZero(zero);
}

countUpFromZero(0);
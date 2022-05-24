eps = 0.01;
fit_eps = 1;

attachment = [5,3,6] + [fit_eps/2, fit_eps/2, fit_eps/2]; //stepper attachment flange
stepper_flange_block = [50,35,10];

servo_lower = [22.6,12,18] + [fit_eps, fit_eps, fit_eps];


difference(){
	translate([-10, -stepper_flange_block[1]/2,0]){
		cube(stepper_flange_block);
	}
	cube(attachment, center=true);
}


difference(){
	translate([stepper_flange_block[0]-10-15, -stepper_flange_block[1]/2,stepper_flange_block[2]-eps]){
		cube([15,stepper_flange_block[1],50]);
	}
	translate([stepper_flange_block[0]-25-eps, -servo_lower[0]/2,stepper_flange_block[2]+50-servo_lower[2]-eps]){
		rotate([90,0,90]){
			    cube(servo_lower);
	    	}
	}
}

color("red"){
}

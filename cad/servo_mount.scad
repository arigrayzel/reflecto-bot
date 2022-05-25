eps = 0.01;
fit_eps = 0.2;

diam=8;
width=4;
flange_width=2;
horn_length=32;


bottom_plate = [horn_length+4,2*horn_length,3];
bottom_width=bottom_plate[2];
inner = [horn_length+2*fit_eps,flange_width+fit_eps,diam+bottom_width];
outer = inner + [4-2*fit_eps,2,4];

difference(){
	translate([-outer[0]/2,-outer[1]/2,0]){cube(outer);}
	translate([-inner[0]/2,-inner[1]/2,-eps]){cube(inner);}
	translate([-diam/2,-diam/2,-eps]){cube([diam,20,diam+bottom_width]);}
}
translate([-outer[0]/2, outer[1]/2-eps,0]){cube(bottom_plate);}

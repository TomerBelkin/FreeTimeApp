import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'side-navbar',
  templateUrl: './side-navbar.component.html',
  styleUrls: ['./side-navbar.component.css']
})
export class SideNavbarComponent implements OnInit {

  isSideNavIsOpen: boolean;

  constructor() { 
    this.openSideNav();
  }

  ngOnInit() {
  }

  openSideNav() {
    this.isSideNavIsOpen = true;
  }

  closeSideNav() {
    this.isSideNavIsOpen = false;
  }

}

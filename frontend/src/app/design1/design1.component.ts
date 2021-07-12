import { Component, OnInit } from '@angular/core';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import {NgbDate, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';

import { DesignComponent } from "../template/design/design.component";

import { ApiService } from "../service/api.service";

@Component({
  selector: 'app-design1',
  templateUrl: './design1.component.html',
  styleUrls: ['./design1.component.css']
})
export class Design1Component extends DesignComponent {

  constructor(calendar: NgbCalendar, api: ApiService) { 
    super(calendar, api)
  }

  onDateSelection(date: NgbDate) {
    if (!this.fromDate && !this.toDate) {
      this.fromDate = date;
    } else if (this.fromDate && !this.toDate && date.after(this.fromDate)) {
      this.toDate = date;
    } else {
      this.toDate = null;
      this.fromDate = date;
    }
  }

  isHovered(date: NgbDate) {
    return this.fromDate && !this.toDate && this.hoveredDate && date.after(this.fromDate) && date.before(this.hoveredDate);
  }

  isInside(date: NgbDate) {
    return this.toDate && date.after(this.fromDate) && date.before(this.toDate);
  }

  isRange(date: NgbDate) {
    return date.equals(this.fromDate) || (this.toDate && date.equals(this.toDate)) || this.isInside(date) || this.isHovered(date);
  }

  // https://ng-bootstrap.github.io/#/components/datepicker/examples

}

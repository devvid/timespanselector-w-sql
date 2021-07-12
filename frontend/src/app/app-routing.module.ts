import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Design1Component } from "./design1/design1.component";


const routes: Routes = [
  { path: 'design1', component: Design1Component },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

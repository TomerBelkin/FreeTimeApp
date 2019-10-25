import { SongDetailComponent } from './song-detail/song-detail.component';
import { NotFondComponent } from './not-fond/not-fond.component';
import { SongsComponent } from './songs/songs.component';
import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  { path: '', redirectTo: '/songs', pathMatch: 'full' },
  { path: 'detail/:id', component: SongDetailComponent },
  { path: 'songs', component: SongsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

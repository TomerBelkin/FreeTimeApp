import { SongsComponent } from './songs/songs.component';
import { SongService } from './services/song.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { NotFondComponent } from './not-fond/not-fond.component';
import { SongDetailComponent } from './song-detail/song-detail.component';
import { SideNavbarComponent } from './side-navbar/side-navbar.component';

@NgModule({
  declarations: [
    AppComponent,
    SongsComponent,
    NotFondComponent,
    SongDetailComponent,
    SideNavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [SongService],
  bootstrap: [AppComponent]
})
export class AppModule { }
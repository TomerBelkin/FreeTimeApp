import { SongsComponent } from './songs/songs.component';
import { SongService } from './services/song.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { NotFondComponent } from './not-fond/not-fond.component';
import { SongDetailComponent } from './song-detail/song-detail.component';
import { SideNavbarComponent } from './side-navbar/side-navbar.component';
import { DownloadSongComponent } from './download-song/download-song.component';

@NgModule({
  declarations: [
    AppComponent,
    SongsComponent,
    NotFondComponent,
    SongDetailComponent,
    SideNavbarComponent,
    DownloadSongComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [SongService],
  bootstrap: [AppComponent]
})
export class AppModule { }
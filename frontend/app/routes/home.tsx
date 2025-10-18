import { Button } from '~/components/ui/button'

import type { Route } from './+types/home'
import GameCard from '~/components/ui/GameCard'
import LandingHeader from '~/home/Home'

export function meta({}: Route.MetaArgs) {
  return [
    { title: 'New React Router App' },
    { name: 'description', content: 'Welcome to React Router!' },
  ]
}

export default function Home() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center">
      <LandingHeader />
    </div>
  )
}

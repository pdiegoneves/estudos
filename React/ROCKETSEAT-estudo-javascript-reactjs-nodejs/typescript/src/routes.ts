import { Request, Response } from 'express'
import createUSer from './services/CreateUser'

export function helloWorld(request: Request, response: Response) {
    const user = createUSer({
        email: 'teste@teste.com',
        password: '123456',
        techs: [
            'Node.js',
            'React.js',
            'React Native',
            {title: 'Javascritp', experience: 100}
        ]
    })

    return response.json({ message: 'Hello World'})
}
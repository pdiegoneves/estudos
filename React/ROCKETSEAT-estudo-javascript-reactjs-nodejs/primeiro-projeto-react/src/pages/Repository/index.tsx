import React from 'react';
import { useRouteMatch, Link } from 'react-router-dom';
import { FiChevronLeft, FiChevronRight } from 'react-icons/fi/';

import logoImg from '../../assets/logo.svg';

import { Header, RepositoryInfo, Issues } from './styles';

interface RepositoryParams {
  repository: string;
}
const Repository: React.FC = () => {
  const { params } = useRouteMatch<RepositoryParams>();
  return (
    <>
      <Header>
        <img src={logoImg} alt="Github explorer" width={40} />
        <Link to="/">
          <FiChevronLeft size={16} /> Voltar
        </Link>
      </Header>
      <RepositoryInfo>
        <header>
          <img src="" alt="" />
          <div>
            <strong>rocket</strong>
            <p>Descrição</p>
          </div>
        </header>
        <ul>
          <li>
            <strong>1808</strong>
            <span>Stars</span>
          </li>
          <li>
            <strong>48</strong>
            <span>Forks</span>
          </li>
          <li>
            <strong>68</strong>
            <span>Issues Abertas</span>
          </li>
        </ul>
      </RepositoryInfo>
      <Issues>
        <Link to="aszs">
          <div>
            <strong>asasd</strong>
            <p>asdasd</p>
          </div>
          <FiChevronRight size={20} />
        </Link>
      </Issues>
    </>
  );
};
export default Repository;
